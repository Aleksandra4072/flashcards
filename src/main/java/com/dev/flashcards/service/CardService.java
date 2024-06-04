package com.dev.flashcards.service;

import com.dev.flashcards.exception.NotFoundException;
import com.dev.flashcards.mapper.CardMapper;
import com.dev.flashcards.model.Card;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

@Service
public class CardService {
    @Autowired
    private final CardMapper cardMapper;

    public CardService(CardMapper cardMapper) {
        this.cardMapper = cardMapper;
    }

    public List<Card> getAllByBundleId(UUID bundleId) {
        List<Card> cards = cardMapper.findALlByBundleId(bundleId);
        return cards == null ?  new ArrayList<>() : cards;
    }

    public void delete(UUID id) {
        Card card = cardMapper.findById(id);
        if (card == null) {
            throw new NotFoundException("Card was not found");
        }

        cardMapper.delete(id);
    }
}
