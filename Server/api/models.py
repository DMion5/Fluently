from django.db import models

class FlashCard(models.Model):
    LANGUAGE_CHOICES = [
        ('EN', 'English'),
        ('ES', 'Spanish'),
        ('FR', 'French'),
        # Add other language codes as needed
    ]

    CERTAINTY_LEVELS = [
        (1, 'Very Low'),
        (2, 'Low'),
        (3, 'Medium'),
        (4, 'High'),
        (5, 'Very High'),
    ]

    question = models.TextField()
    answer = models.TextField()
    category = models.CharField(max_length=100)
    source_language = models.CharField(
        max_length=2,
        choices=LANGUAGE_CHOICES,
        default='ES'  # Default is Spanish
    )
    target_language = models.CharField(
        max_length=2,
        choices=LANGUAGE_CHOICES,
        default='EN'  # Default is English
    )

    # New certainty field
    certainty = models.IntegerField(
        choices=CERTAINTY_LEVELS,
        default=3,  # Default to 'Medium' certainty level
        help_text="How confidently the user knows this flashcard (1-5 scale)"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    last_reviewed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.category} - {self.question[:50]} ({self.source_language}->{self.target_language}) - Certainty: {self.certainty}"

    class Meta:
        ordering = ['-created_at']
