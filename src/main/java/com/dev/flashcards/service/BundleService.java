package com.dev.flashcards.service;

import com.dev.flashcards.mapper.BundleMapper;
import com.dev.flashcards.mapper.CardMapper;
import com.dev.flashcards.model.Bundle;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

@Service
public class BundleService {
    @Autowired
    private final BundleMapper bundleMapper;
    private final CardMapper cardMapper;

    public BundleService(CardMapper cardMapper, BundleMapper bundleMapper) {
        this.cardMapper = cardMapper;
        this.bundleMapper = bundleMapper;
    }

    public List<Bundle> getAll(UUID userId) {
        List<Bundle> bundles = bundleMapper.findALlByUserID(userId);
        return bundles == null ?  new ArrayList<>() : bundles;
    }
}
