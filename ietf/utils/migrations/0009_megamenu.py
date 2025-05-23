# Generated by Django 4.2.7 on 2023-12-18 08:56

import uuid

import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.models
from django.db import migrations, models


def populate_main_menu(apps, schema_editor):
    Page = apps.get_model("wagtailcore.Page")
    HomePage = apps.get_model("home.HomePage")
    MainMenuItem = apps.get_model("utils.MainMenuItem")

    def live_children(page):
        if not page:
            return Page.objects.none()
        # path of children is path of parent with 4 more characters at the end
        return (
            Page.objects.filter(path__regex=f"^{page.path}....$")
            .filter(live=True)
            .order_by("path")
        )

    homepage = HomePage.objects.first()
    if not homepage:
        return

    menu_pages = live_children(homepage).filter(show_in_menus=True)
    for sort_order, page in enumerate(menu_pages, start=1):
        secondary_sections = []
        for child in live_children(page):
            subchildren = list(live_children(child).filter(show_in_menus=True))
            if subchildren:
                secondary_sections.append(
                    {
                        "id": str(uuid.uuid4()),
                        "type": "section",
                        "value": {
                            "title": child.title,
                            "links": [
                                {
                                    "id": str(uuid.uuid4()),
                                    "type": "item",
                                    "value": {
                                        "page": subchild.pk,
                                        "title": "",
                                        "external_url": "",
                                    },
                                }
                                for subchild in subchildren
                            ],
                        },
                    },
                )

        MainMenuItem.objects.create(
            page=page,
            sort_order=sort_order * 10,
            secondary_sections=secondary_sections,
        )


class Migration(migrations.Migration):

    dependencies = [
        ("images", "0004_django_42_rendition_storage"),
        ("wagtailcore", "0089_log_entry_data_json_null_to_object"),
        ("utils", "0008_socialmediasettings_github_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="MenuItem",
            new_name="SecondaryMenuItem",
        ),
        migrations.CreateModel(
            name="MainMenuItem",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "secondary_sections",
                    wagtail.fields.StreamField(
                        [
                            (
                                "section",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "title",
                                            wagtail.blocks.CharBlock(
                                                label="Section title", required=True
                                            ),
                                        ),
                                        (
                                            "links",
                                            wagtail.blocks.ListBlock(
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "page",
                                                            wagtail.blocks.PageChooserBlock(
                                                                label="Page",
                                                                required=False,
                                                            ),
                                                        ),
                                                        (
                                                            "title",
                                                            wagtail.blocks.CharBlock(
                                                                label="Link text",
                                                                required=False,
                                                            ),
                                                        ),
                                                        (
                                                            "external_url",
                                                            wagtail.blocks.URLBlock(
                                                                label="External URL",
                                                                required=False,
                                                            ),
                                                        ),
                                                    ]
                                                )
                                            ),
                                        ),
                                    ]
                                ),
                            )
                        ],
                        blank=True,
                        use_json_field=True,
                    ),
                ),
                ("sort_order", models.PositiveSmallIntegerField()),
                (
                    "image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="images.ietfimage",
                    ),
                ),
                (
                    "page",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="wagtailcore.page",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
            },
            bases=(wagtail.models.PreviewableMixin, models.Model),
        ),
        migrations.RunPython(populate_main_menu, migrations.RunPython.noop),
    ]
