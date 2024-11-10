from django.db import models

class FlashCard(models.Model):
    LANGUAGE_CHOICES = [
        ('EN', 'English'),
        ('ES', 'Spanish'),
        ('FR', 'French'),
        # Add other language codes as needed
    ]

    DIFFICULTY_CHOICES = [
        ('E', 'Easy'),
        ('M', 'Medium'),
        ('H', 'Hard'),
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
    difficulty = models.CharField(
        max_length=1,
        choices=DIFFICULTY_CHOICES,
        default='M'  # Default is Medium difficulty
    )
    source_set = models.CharField(
        max_length=100,
        default="default_set",  # Set the default value for new records
        help_text="The source set or deck for the flashcard"
    )

    priority_in_set = models.IntegerField(default=0, help_text="The priority of the card in the set (used for sorting)")
    language = models.CharField(
        max_length=2,
        choices=LANGUAGE_CHOICES,
        default='ES'  # Default to Spanish
    )
    certainty = models.IntegerField(
        choices=CERTAINTY_LEVELS,
        default=3,  # Default to 'Medium' certainty level
        help_text="How confidently the user knows this flashcard (1-5 scale)"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    last_reviewed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.source_set} - {self.question[:50]} ({self.language}) - Certainty: {self.certainty}"

    class Meta:
        ordering = ['priority_in_set', '-created_at']  # Sort by priority_in_set first, then by created_at

