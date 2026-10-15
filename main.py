import fastapi as _fastapi
from typing import TYPE_CHECKING, List
import sqlalchemy.orm as _orm
import services as _services
import schemas as _schemas
from  fastapi.responses import HTMLResponse


if TYPE_CHECKING:
    from sqlalchemy.orm import Session



app = _fastapi.FastAPI()

_services._add_tables()

@app.post("/api/contacts/", response_model = _schemas.Contact)
async def create_contact(contact: _schemas.CreateContact, db: _orm.Session = _fastapi.Depends(_services.get_db),
                         ):
    return await _services.create_contact(contact = contact , db = db)


@app.get("/api/contacts/", response_model = List[_schemas.Contact])
async def get_contacts( db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.get_all_contacts(db =db)


@app.get("/api/contacts/{contact_id}/", response_model = _schemas.Contact)
async def get_contact(contact_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db) ):
    return await _services.get_contact(contact_id = contact_id, db=db)


@app.delete("/api/contacts/{contact_id}/")
async def delete_contact(contact_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db) ):
    contact = await _services.get_contact(db = db, contact_id = contact_id )
    if contact is None :
        raise _fastapi.HTTPException(status_code = 404 , detail = "Contact does not exist in database")
    
    await  _services.delete_contact(contact, db = db)

    return "Succesfully deleted user." 

@app.put("/api/contacts/{contact_id}/", response_model = _schemas.Contact)
async def update_contact( contact_id : int,  contact_data : _schemas.CreateContact, db : _orm.Session = _fastapi.Depends(_services.get_db)):
    contact = await _services.get_contact(db = db, contact_id = contact_id )
    if contact is None :
        raise _fastapi.HTTPException(status_code = 404 , detail = "Contact does not exist in database")
    return await _services.update_contact(contact_data = contact_data, contact = contact, db = db)
    
@app.get("/contacts/", response_class=HTMLResponse)
async def get_contacts_html( db: _orm.Session = _fastapi.Depends(_services.get_db)):
    contacts = await _services.get_all_contacts(db =db)
    s = """
    <html>
    <head>
        <title>Contacts</title>
        <style>
            body { 
                font-family: verdana;
                color: #1e293b; 
                max-width: 600px; 
                margin: 40px auto; 
                padding: 0 20px; 
            }
            h1 { 
                font-size: 24px; 
                font-weight: 600; 
            }
            
            .card { 
                background: #ffffff; 
                border: 1px solid #e2e8f0; 
                box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
                padding:20px;
           }
        </style>
    </head>
    <body>
        <h1>Contacts</h1>
        <div class="card-list">
    """
    
    for i, contact in enumerate(contacts, start = 1):
        s += f"""
            <div class="card"  onmouseover="this.style.backgroundColor='#e0f2fe'" onmouseout="this.style.backgroundColor='white'">
            {i}.<b>{contact.first_name} {contact.last_name}</b>
                <br/>         
                     tel: <em>{contact.phone_number}</em>
                    <br/>
                     email: <a href='emailto:{contact.email}'>{contact.email}</a>
                 <br/>
            </div>
        """
        
    s += """
        </div>
    </body>
    </html>
    """
    return s
