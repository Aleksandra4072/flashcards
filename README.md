In "/src/main/resources" create "application.properties" file and add:

```
    spring.application.name=flashcards

    spring.datasource.driver-class-name=org.postgresql.Driver
    spring.datasource.url=url
    spring.datasource.username=username
    spring.datasource.password=password
    
    spring.flyway.url=url
    spring.flyway.user=username
    spring.flyway.password=password
    spring.flyway.enabled=true
    spring.flyway.locations=classpath:db/migration

```

---