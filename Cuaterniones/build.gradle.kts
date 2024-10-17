plugins {
    kotlin("jvm") version "1.8.0"
    java
    id("jacoco")
}

repositories {
    mavenCentral()
}

dependencies {
    testImplementation(kotlin("test"))
}

java {
    sourceCompatibility = JavaVersion.VERSION_1_8
    targetCompatibility = JavaVersion.VERSION_1_8
}

tasks.withType<org.jetbrains.kotlin.gradle.tasks.KotlinCompile> {
    kotlinOptions {
        jvmTarget = "1.8"
    }
}

tasks.test {
    useJUnitPlatform()
    finalizedBy(tasks.jacocoTestReport) // Generar el reporte de JaCoCo después de las pruebas
}

tasks.jacocoTestReport {
    dependsOn(tasks.test) // Ejecutar las pruebas antes de generar el reporte
    reports {
        xml.required.set(true)
        html.required.set(true)
    }
}