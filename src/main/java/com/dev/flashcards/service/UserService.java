package com.dev.flashcards.service;

import com.dev.flashcards.exception.NotFoundException;
import com.dev.flashcards.mapper.BundleMapper;
import com.dev.flashcards.mapper.CardMapper;
import com.dev.flashcards.mapper.UserMapper;
import com.dev.flashcards.model.Bundle;
import com.dev.flashcards.model.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

@Service
public class UserService {

    @Autowired
    private final UserMapper userMapper;
    private final BundleMapper bundleMapper;
    private final CardMapper cardMapper;

    public UserService(UserMapper userMapper, BundleMapper bundleMapper, CardMapper cardMapper) {
        this.userMapper = userMapper;
        this.bundleMapper = bundleMapper;
        this.cardMapper = cardMapper;
    }

    public List<User> getAll() {
        List<User> users = userMapper.findALl();
        return users == null ?  new ArrayList<>() : users;
    }

    public User getById(UUID id) {
        User user = userMapper.findById(id);
        if (user == null) {
            throw new NotFoundException("User with ID " + id + " not found");
        }
        return user;
    }

    public void delete(UUID id) {
        User user  = userMapper.findById(id);
        if (user == null ) {
            throw new NotFoundException("User with ID " + id + " not found");
        }

        List<Bundle> bundles = bundleMapper.findALlByUserID(id);
        for (Bundle bundle : bundles) {
            cardMapper.deleteByBundleId(UUID.fromString(bundle.getId()));
        }

        bundleMapper.deleteByUserId(id);

        userMapper.delete(id);
    }
}
