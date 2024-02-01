import boto3

db = boto3.resource('dynamodb')
table = db.Table("employees")

## add data to the table
# table.put_item(
#     Item={
#         'emp_id':"2",
#         'name':"Shraddha Khadepatil",
#         'age':"28"
#     }
# )

# get the data from the table
response = table.get_item(
    Key={
        'emp_id':"2"
    }
)

print(response["Item"]["name"])


