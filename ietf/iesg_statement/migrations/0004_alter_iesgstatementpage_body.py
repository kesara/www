# Generated by Django 3.2.10 on 2022-01-06 21:31

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.contrib.typed_table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtailmarkdown.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('iesg_statement', '0003_auto_20211101_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iesgstatementpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image', template='includes/imageblock.html')), ('markdown', wagtailmarkdown.blocks.MarkdownBlock(icon='code')), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='code')), ('raw_html', wagtail.core.blocks.RawHTMLBlock(icon='placeholder')), ('table', wagtail.contrib.table_block.blocks.TableBlock(table_options={'renderer': 'html'}, template='includes/tableblock.html')), ('typed_table', wagtail.contrib.typed_table_block.blocks.TypedTableBlock([('text', wagtail.core.blocks.CharBlock()), ('numeric', wagtail.core.blocks.FloatBlock()), ('rich_text', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image', template='includes/imageblock.html'))]))]),
        ),
    ]
