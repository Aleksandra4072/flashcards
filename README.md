In "/src/main/resources" create "application.properties" file and add:

```

    spring.application.name=<application_name>

    spring.datasource.driver-class-name=<db_driver>
    spring.datasource.url=<db_url>
    spring.datasource.username=<username>
    spring.datasource.password=<password>
    
    spring.flyway.url=<db_url>
    spring.flyway.user=<username>
    spring.flyway.password=<password>
    spring.flyway.enabled=<true/false>
    spring.flyway.locations=<classpath:db/migration>
    
    jwt.key=<jwt_key>
    jwt.expiration-time=<jwt_expiration_time_in_milliseconds>
    
    spring.security.user.password=<default_password>
    spring.security.user.name=<default_user>

```

---