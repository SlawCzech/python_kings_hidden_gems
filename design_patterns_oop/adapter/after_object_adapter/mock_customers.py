from design_patterns_oop.adapter.after_object_adapter.cust_adapter import CustomerAdapter
from design_patterns_oop.adapter.after_object_adapter.customer import Customer

MOCKCUSTOMERS = (
    CustomerAdapter(Customer('Pizza Love', '33 Pepperoni Lane')),
    CustomerAdapter(Customer('Happy and Green', '25 Kale St.')),
    CustomerAdapter(Customer('Sweet Tooth', '42 Chocolate Ave.'))
)
