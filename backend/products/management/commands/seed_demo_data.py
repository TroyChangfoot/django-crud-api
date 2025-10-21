from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker
import random

from products.models import Product
from customers.models import Customer
from orders.models import Order, OrderItem


class Command(BaseCommand):
    help = "Seeds demo data (products, customers, orders) for local testing."

    def add_arguments(self, parser):
        parser.add_argument("--products", type=int, default=10, help="Number of products to create")
        parser.add_argument("--customers", type=int, default=5, help="Number of customers to create")
        parser.add_argument("--orders", type=int, default=10, help="Number of orders to create")

    @transaction.atomic
    def handle(self, *args, **options):
        fake = Faker()
        num_products = options["products"]
        num_customers = options["customers"]
        num_orders = options["orders"]

        self.stdout.write(self.style.NOTICE("Seeding demo data..."))

        # --- Products ---
        Product.objects.all().delete()
        products = []
        for _ in range(num_products):
            product = Product(
                name=fake.word().capitalize() + " " + fake.word().capitalize(),
                description=fake.sentence(),
                sku=f"P{random.randint(1000, 9999)}",
                price=round(random.uniform(20.0, 500.0), 2),
                stock=random.randint(5, 100),
                is_active=True,
            )
            products.append(product)
        Product.objects.bulk_create(products)
        self.stdout.write(self.style.SUCCESS(f"✅ Created {num_products} products"))

        # --- Customers ---
        Customer.objects.all().delete()
        customers = []
        for _ in range(num_customers):
            customer = Customer(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email(),
                phone=fake.phone_number(),
                address=fake.street_address(),
                city=fake.city(),
                country=fake.country(),
            )
            customers.append(customer)
        Customer.objects.bulk_create(customers)
        self.stdout.write(self.style.SUCCESS(f"✅ Created {num_customers} customers"))

        # --- Orders ---
        Order.objects.all().delete()
        for _ in range(num_orders):
            customer = random.choice(Customer.objects.all())
            order = Order.objects.create(
                customer=customer,
                status=random.choice([Order.Status.PENDING, Order.Status.PAID, Order.Status.SHIPPED]),
                total_amount=0,
            )

            for _ in range(random.randint(1, 4)):
                product = random.choice(Product.objects.all())
                qty = random.randint(1, 3)
                price = product.price
                OrderItem.objects.create(order=order, product=product, quantity=qty, price=price)
                order.total_amount += qty * price

            order.save()

        self.stdout.write(self.style.SUCCESS(f"✅ Created {num_orders} orders with line items"))
        self.stdout.write(self.style.SUCCESS("🎉 Demo data seeding completed!"))
