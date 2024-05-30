package com.dev.flashcards;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@MapperScan("com.dev.flashcards.mapper")
@SpringBootApplication
public class FlashcardsApplication {
	public static void main(String[] args) {
		SpringApplication.run(FlashcardsApplication.class, args);
	}
}
