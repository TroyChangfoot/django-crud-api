from rest_framework import serializers
from .models import Order, OrderItem
from products.models import Product


class OrderItemSerializer(serializers.ModelSerializer):
    """Serializer for individual order line items."""
    product_name = serializers.ReadOnlyField(source="product.name")
    price = serializers.DecimalField(
        max_digits=10, decimal_places=2, required=False
    )  # optional incase of price over-ride / discount processing wip

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "product",
            "product_name",
            "quantity",
            "price",
            "get_line_total",
        ]


class OrderSerializer(serializers.ModelSerializer):
    """Serializer for orders with nested order items."""
    customer_name = serializers.ReadOnlyField(source="customer.first_name")
    items = OrderItemSerializer(many=True, required=False)

    class Meta:
        model = Order
        fields = [
            "id",
            "customer",
            "customer_name",
            "status",
            "total_amount",
            "items",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["total_amount", "created_at", "updated_at"]

    def create(self, validated_data):
        """Create order with nested order items and auto-calc total."""
        items_data = validated_data.pop("items", [])
        order = Order.objects.create(**validated_data)
        total = 0

        for item_data in items_data:
            product = item_data["product"]
            quantity = item_data.get("quantity", 1)

            # Use product price if none provided
            price = item_data.get("price") or product.price
            total += quantity * price

            OrderItem.objects.create(
                order=order, product=product, quantity=quantity, price=price
            )

        order.total_amount = total
        order.save()
        return order

    def update(self, instance, validated_data):
        """Update order and its nested items, recalculating totals."""
        items_data = validated_data.pop("items", None)
        instance.status = validated_data.get("status", instance.status)
        instance.customer = validated_data.get("customer", instance.customer)
        instance.save()

        if items_data is not None:
            instance.items.all().delete()
            total = 0
            for item_data in items_data:
                product = item_data["product"]
                quantity = item_data.get("quantity", 1)
                price = item_data.get("price") or product.price
                total += quantity * price
                OrderItem.objects.create(
                    order=instance,
                    product=product,
                    quantity=quantity,
                    price=price,
                )
            instance.total_amount = total
            instance.save()

        return instance
