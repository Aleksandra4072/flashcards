package com.dev.flashcards.controller;

import com.dev.flashcards.model.Bundle;
import com.dev.flashcards.service.BundleService;
import io.swagger.v3.oas.annotations.Operation;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.UUID;

@RestController
@RequestMapping("/bundles")
public class BundleController {
    private final BundleService bundleService;

    public BundleController(BundleService bundleService) {
        this.bundleService = bundleService;
    }

    @Operation(summary = "Get all the bundles of a user", description = "Returns a list of bundles")
    @GetMapping("/{userId}")
    public List<Bundle> getAllByUserId(@PathVariable String userId) {
        UUID uuid = UUID.fromString(userId);
        return bundleService.getAll(uuid);
    }
}
