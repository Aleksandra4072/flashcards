package com.dev.flashcards.controller;

import com.dev.flashcards.model.Card;
import com.dev.flashcards.service.CardService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.security.SecurityRequirement;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@SecurityRequirement(name = "bearerAuth")
@Tag(name = "Cards")
@RestController
@RequestMapping("/cards")
public class CardController {
    private final CardService cardService;

    public CardController(CardService cardService) {
        this.cardService = cardService;
    }


    @Operation(summary = "Get all the cards of a certain bundle", description = "Returns a list of cards of bundle")
    @GetMapping("/{bundleId}")
    public List<Card> getAllByBundle(@PathVariable String bundleId) {
        return cardService.getAllByBundleId(bundleId);
    }

    @Operation(summary = "Delete card", description = "Delete card")
    @DeleteMapping("/{id}")
    public void delete(@PathVariable String id) {
        cardService.delete(id);
    }
}
