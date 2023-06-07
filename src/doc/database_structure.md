// Use DBML to define your database structure
// Docs: https://dbml.dbdiagram.io/docs

Table customer {
  id integer [primary key]
  name integer
  first_name varchar
  last_name varchar
  address_1 varchar
  address_2 varchar
  city varchar
  zip_code varchar
  phone_number varchar
  email varchar
  jib varchar
  pib varchar
  created_at timestamp
  modified_at timestamp
  active bool
}

Table payment {
  id integer [primary key]
  person_id integer [ref: > person.id]
  bill_id varchar
  payment_details_id integer [ref: - payment_details.id]
  customer_id integer [ref: > customer.id]
  ciy varchar
  date_of_issue timestamp
  value_date timestamp
  delivery_date timestamp
  payment_method varchar
  content json [note: 'This is content of products']
}

Table payment_details {
  id integer [primary key] 
  total_amount varchar
  created_at timestamp
  modified_at timestamp
}

Table payment_items {
  id integer [primary key]
  payment_id integer [ref: > payment.id]
  created_at timestamp
  modified_at timestamp
}

Table person {
  id integer [primary key]
  first_name varchar
  last_name varchar
  email varchar
  phone_number varchar
  user integer [ref: - user.id]
  active bool
  created_at timestamp
  modified_at timestamp
}

Table user {
  id integer [primary key]
  username varchar
  is_staff bool
  is_active bool
  is_superuser bool
}