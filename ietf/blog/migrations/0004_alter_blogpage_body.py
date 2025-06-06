# Generated by Django 3.2.13 on 2022-09-02 04:24

import wagtail.blocks
import wagtail.contrib.table_block.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtailmarkdown.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_auto_20211101_0113"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    ("heading", wagtail.blocks.CharBlock(icon="title")),
                    ("paragraph", wagtail.blocks.RichTextBlock(icon="pilcrow")),
                    (
                        "image",
                        wagtail.images.blocks.ImageChooserBlock(
                            icon="image", template="includes/imageblock.html"
                        ),
                    ),
                    ("markdown", wagtailmarkdown.blocks.MarkdownBlock(icon="code")),
                    ("embed", wagtail.embeds.blocks.EmbedBlock(icon="code")),
                    ("raw_html", wagtail.blocks.RawHTMLBlock(icon="placeholder")),
                    (
                        "table",
                        wagtail.contrib.table_block.blocks.TableBlock(
                            table_options={"renderer": "html"},
                            template="includes/tableblock.html",
                        ),
                    ),
                ],
                use_json_field=True,
            ),
        ),
    ]
