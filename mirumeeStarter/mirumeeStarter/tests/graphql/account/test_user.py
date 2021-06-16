from ....account.models import User
import json

def test_user_mutation(db, client_query, usermutation):

    response = client_query(
        """
        mutation usermutation{
            userCreate(input: {
                email: "test@test.com",
                firstName: "Test",
                lastName: "Test",
                password: "qwerty123456A$"
            }){
            user{
                id,
                email,
                firstName,
                lastName,
                password
            }
                
            }
        }

        """
    )

    content = json.loads(response.content)

    response_content = content['data']['userCreate']['user']
    
    assert response_content['id'] == str(usermutation.id)
    assert response_content['email'] == usermutation.email
    assert response_content['firstName'] == usermutation.firstName
    assert response_content['lastName'] == usermutation.lastName
    assert response_content['password'] == usermutation.password