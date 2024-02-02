import boto3

db = boto3.resource('dynamodb')
table = db.Table("employees")

# add data to the table
# table.put_item(
#     Item={
#         'emp_id':"4",
#         'name':"Sarvesh Kulkarni",
#         'age':"29"
#     }
# )

# get the data from the table
response = table.get_item(
    Key={
        'emp_id':"4"
    }
)

print(response["Item"]["name"])


