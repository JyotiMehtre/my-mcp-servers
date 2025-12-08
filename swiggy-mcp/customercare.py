from mcp.server.fastmcp import FastMCP
from customers import CUSTOMERS
from orders import ORDERS
from restaurants import RESTARAUNTS

mcp = FastMCP(
    name="swiggy-mcp",
    website_url="https://github.com/JyotiMehtre"
)

# ============================
#           TOOLS
# ============================

@mcp.tool()
def get_customer_summary(customer_id: str) -> dict|None:
    for customer in CUSTOMERS:
        if customer['customerId'] == customer_id:
            return customer
        return None
            
 

@mcp.tool()
def get_order_information(order_id: str) -> dict|None:
     for order in ORDERS:
        if order['orderId'] == order_id:
            return order
        return None
      
  


@mcp.tool()
def get_restaurant_information(restaurant_id: str) -> dict|None:
       for restaurant in RESTARAUNTS:
        if restaurant['restaurantId'] == restaurant_id:
            return restaurant
        return None
      
   
# ============================
#         RESOURCES
# ============================

@mcp.resource("policy://refund")
def get_refund_policy() -> str:
    lines = []
    with open('refundpolicy.md') as refund:
        lines = refund.readlines()
    return "\n".join(lines)


@mcp.resource("complaint://{ctype}")
def get_complaint_resolution(ctype) -> str:
    lines = []
    with open('latetimedelivery.md') as refund:
        lines = refund.readlines()
    return "\n".join(lines)

if __name__ == "__main__":
    mcp.run(transport="stdio")
