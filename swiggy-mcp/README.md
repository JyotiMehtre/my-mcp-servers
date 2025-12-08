# 🍔 Swiggy-MCP – Customer Support MCP Server

This is a custom **MCP (Model Context Protocol)** server that simulates a basic **Swiggy customer support system**.  
It exposes tools that allow an AI (like Claude Desktop) to fetch customer order details, complaints, and summary info.

---

## 🚀 Features

- Connects directly with **Claude Desktop** via MCP.
- Provides APIs such as:
  - `get_customer_summary(customer_id)`
  - `get_order_status(order_id)`
  - `raise_complaint(order_id, issue)`
- Clean Python structure using `FastMCP`.
- Easy to extend with new tools.

---