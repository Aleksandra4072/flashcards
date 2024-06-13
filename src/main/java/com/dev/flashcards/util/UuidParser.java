package com.dev.flashcards.util;

import java.util.UUID;

public class UuidParser {

    public static UUID parse(String input) {
        return UUID.fromString(input);
    }
}
