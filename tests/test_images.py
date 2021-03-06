"""Tests for image generation."""

# pylint: disable=bad-continuation

from pathlib import Path


SAMPLES = Path(__file__).parent.joinpath("samples")


def test_samples(client):
    """Create various sample images for manual verfification."""
    for name, url in [
        ("basic.jpg", "/ch/hello/world.jpg"),
        ("nominal.jpg", "/ch/a-normal-line-of-top-meme-text-followed-by/"
            "another-normal-line-of-bottom-meme-text.jpg"),
        ("long.jpg", "/ch/" + ("long-" * 15) + "line/short-line.jpg"),
        ("subscripts.jpg", "/ch/some-unicode-subscripts/h%E2%82%82o.jpg"),
    ]:
        save_image(client, url, name)


def test_impact_font(client):
    """Create a meme using a custom font.

    See: https://github.com/jacebrowning/memegen/issues/216

    """
    url = "/ch/we-like-using-the/custom-fonts.jpg?font=impact"
    save_image(client, url, "impact.jpg")


def save_image(client, url, name):
    response = client.get(url)
    data = response.get_data()

    with SAMPLES.joinpath(name).open('wb') as image:
        image.write(data)
