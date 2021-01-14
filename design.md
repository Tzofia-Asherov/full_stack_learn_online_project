```plantuml
@startuml

component server
component view
actor student
actor teacher
database db
server-db
view-server
student--view
teacher--view
@enduml
```