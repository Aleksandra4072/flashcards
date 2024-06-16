package com.dev.flashcards.controller;

import com.dev.flashcards.model.Bundle;
import com.dev.flashcards.service.BundleService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.security.SecurityRequirement;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@SecurityRequirement(name = "bearerAuth")
@Tag(name = "Bundles")
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
        return bundleService.getAllByUserId(userId);
    }

    @Operation(summary = "Get the bundles by id", description = "Returns a certain bundles")
    @GetMapping("")
    public Bundle getAllById(@RequestParam(name = "id") String id) {
        return bundleService.getById(id);
    }

    @Operation(summary = "Deleting bundle with it's cards", description = "Deleting bundle")
    @DeleteMapping("/{id}")
    public void deleteById(@PathVariable String id) {
        bundleService.delete(id);
    }
}
