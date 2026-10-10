from datetime import datetime
from database import ORDERS_DB

def get_order_details(order_id: str) -> dict:
    """Fetch order details by order ID."""
    order = ORDERS_DB.get(order_id.strip().upper())
    if not order:
        return {"error": f"Order {order_id} not found."}
    return order

def check_return_eligibility(order_id: str) -> dict:
    """Check if an order is eligible for return based on policy."""
    order = ORDERS_DB.get(order_id.strip().upper())
    if not order:
        return {"eligible": False, "reason": "Order not found."}

    if order["status"] != "DELIVERED":
        return {
            "eligible": False,
            "reason": f"Order is currently '{order['status']}'. Returns are only permitted for delivered items."
        }

    delivery_date = datetime.strptime(order["delivery_date"], "%Y-%m-%d")
    days_since_delivery = (datetime.now() - delivery_date).days

    if days_since_delivery > order["return_window_days"]:
        return {
            "eligible": False,
            "reason": f"Delivery was {days_since_delivery} days ago, exceeding the {order['return_window_days']}-day return window."
        }

    return {
        "eligible": True,
        "reason": f"Delivered {days_since_delivery} days ago. Within valid {order['return_window_days']}-day window."
    }

def initiate_return(order_id: str, return_reason: str) -> dict:
    """Initiates a return for a verified eligible order."""
    eligibility = check_return_eligibility(order_id)
    if not eligibility["eligible"]:
        return {"success": False, "message": eligibility["reason"]}

    order = ORDERS_DB[order_id.strip().upper()]
    order["return_status"] = "RETURN_REQUESTED"
    order["return_reason"] = return_reason
    return {
        "success": True,
        "message": f"Return successfully initiated for order {order['order_id']}. Return pickup scheduled within 48 hours."
    }

def cancel_order(order_id: str, cancellation_reason: str) -> dict:
    """Cancels an order if it has not yet been shipped or delivered."""
    order = ORDERS_DB.get(order_id.strip().upper())
    if not order:
        return {"success": False, "message": f"Order {order_id} not found."}

    if order["status"] in ["SHIPPED", "DELIVERED"]:
        return {
            "success": False,
            "message": f"Cannot cancel order {order_id}. Current status is '{order['status']}'. Once shipped, items can only be returned after delivery."
        }

    order["status"] = "CANCELLED"
    order["cancellation_reason"] = cancellation_reason
    return {
        "success": True,
        "message": f"Order {order_id} has been successfully cancelled. Refund initiated to original payment method."
    }

def update_shipping_address(order_id: str, new_address: str) -> dict:
    """Updates the delivery address if the order has not been dispatched yet."""
    order = ORDERS_DB.get(order_id.strip().upper())
    if not order:
        return {"success": False, "message": f"Order {order_id} not found."}

    if order["status"] in ["SHIPPED", "DELIVERED", "CANCELLED"]:
        return {
            "success": False,
            "message": f"Cannot update address for order {order_id} because status is '{order['status']}'."
        }

    old_address = order["shipping_address"]
    order["shipping_address"] = new_address.strip()
    return {
        "success": True,
        "message": f"Shipping address for order {order_id} updated from '{old_address}' to '{new_address}'."
    }

def escalate_to_human(order_id: str, reason: str) -> dict:
    """Escalates complex issues or exceptions to human support staff."""
    return {
        "escalated": True,
        "ticket_id": f"TICK-{datetime.now().strftime('%H%M%S')}",
        "summary": f"Escalated order {order_id}: {reason}"
    }

AVAILABLE_TOOLS = {
    "get_order_details": get_order_details,
    "check_return_eligibility": check_return_eligibility,
    "initiate_return": initiate_return,
    "cancel_order": cancel_order,
    "update_shipping_address": update_shipping_address,
    "escalate_to_human": escalate_to_human
}