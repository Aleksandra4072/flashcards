package com.dev.flashcards.service;

import com.dev.flashcards.exception.NotFoundException;
import com.dev.flashcards.mapper.BundleMapper;
import com.dev.flashcards.mapper.CardMapper;
import com.dev.flashcards.model.Bundle;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

@Service
public class BundleService {
    private final BundleMapper bundleMapper;
    private final CardMapper cardMapper;

    public BundleService(CardMapper cardMapper, BundleMapper bundleMapper) {
        this.cardMapper = cardMapper;
        this.bundleMapper = bundleMapper;
    }

    public List<Bundle> getAllByUserId(String userId) {
        List<Bundle> bundles = bundleMapper.findALlByUserID(UUID.fromString(userId));
        return bundles == null ?  new ArrayList<>() : bundles;
    }

    public Bundle getById(String id) {
        Bundle bundle = bundleMapper.findById(UUID.fromString(id));

        if (bundle == null) {
            throw new NotFoundException("Bundle was not found");
        }
        return bundle;
    }

    public void delete(String id) {
        Bundle bundle = bundleMapper.findById(UUID.fromString(id));

        if (bundle == null) {
            throw new NotFoundException("Bundle was not found");
        }
        cardMapper.deleteByBundleId(UUID.fromString(id));
        bundleMapper.deleteById(UUID.fromString(id));
    }
}
