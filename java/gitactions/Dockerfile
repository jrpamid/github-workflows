FROM maven:3.8-jdk-8 as builder

WORKDIR /app
COPY pom.xml .
COPY src ./src

# Build a release artifact.
RUN mvn package -DskipTests

FROM adoptopenjdk/openjdk8:alpine-jre

# Copy the jar to the production image from the builder stage.
COPY --from=builder /app/target/gitactions-*.jar /gitactions.jar

# Run the web service on container startup.
CMD ["java", "-Djava.security.egd=file:/dev/./urandom", "-jar", "/gitactions.jar"]