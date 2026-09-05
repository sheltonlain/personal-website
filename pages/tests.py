from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_templates_used(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")
        self.assertTemplateUsed(response, "base.html")

    def test_page_lists_at_least_five_items(self):
        response = self.client.get(reverse("home"))
        html = response.content.decode()
        self.assertGreaterEqual(html.count("<li>"), 5)

    def test_page_shows_both_status_labels(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Completed")
        self.assertContains(response, "In progress")


class AboutPageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_templates_used(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")
        self.assertTemplateUsed(response, "base.html")

    def test_page_contains_heading(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "About Me")


class ContactPageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)

    def test_templates_used(self):
        response = self.client.get(reverse("contact"))
        self.assertTemplateUsed(response, "contact.html")
        self.assertTemplateUsed(response, "base.html")

    def test_page_contains_heading(self):
        response = self.client.get(reverse("contact"))
        self.assertContains(response, "Contact")


class NavigationTests(SimpleTestCase):
    def test_every_page_links_to_every_page(self):
        for page_name in ["home", "about", "contact"]:
            response = self.client.get(reverse(page_name))
            self.assertContains(response, reverse("home"))
            self.assertContains(response, reverse("about"))
            self.assertContains(response, reverse("contact"))

