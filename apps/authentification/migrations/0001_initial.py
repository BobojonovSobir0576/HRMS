# Generated by Django 4.2.7 on 2023-12-27 11:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar/')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'CustomUser',
                'verbose_name_plural': 'CustomUsers',
                'db_table': 'table_user',
            },
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Countries',
                'verbose_name_plural': 'Countries',
                'db_table': 'table_countries',
            },
        ),
        migrations.CreateModel(
            name='HrCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo/')),
                ('content', models.TextField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('countries', models.ManyToManyField(blank=True, null=True, related_name='countrycompany', to='authentification.countries')),
                ('hrs', models.ManyToManyField(blank=True, null=True, related_name='hrsusers', to=settings.AUTH_USER_MODEL)),
                ('sub_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcompany', to='authentification.hrcompany')),
                ('users', models.ManyToManyField(blank=True, null=True, related_name='companyuser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
                'db_table': 'table_companies',
            },
        ),
        migrations.CreateModel(
            name='JobApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Job Apply',
                'verbose_name_plural': 'Job Apply',
                'db_table': 'table_job_apply',
            },
        ),
        migrations.CreateModel(
            name='JobCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Job Category',
                'verbose_name_plural': 'Job Categories',
                'db_table': 'table_job_categories',
            },
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Job Type',
                'verbose_name_plural': 'Job Types',
                'db_table': 'table_job_type',
            },
        ),
        migrations.CreateModel(
            name='LevelEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Level Education',
                'verbose_name_plural': 'Level Education',
                'db_table': 'table_level_education',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Role',
                'db_table': 'table_role',
            },
        ),
        migrations.CreateModel(
            name='StatusApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Status Apply',
                'verbose_name_plural': 'Status Apply',
                'db_table': 'table_status_apply',
            },
        ),
        migrations.CreateModel(
            name='SmsHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='smscode', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'History User code',
                'verbose_name_plural': 'History User codes',
                'db_table': 'table_sms_history',
            },
        ),
        migrations.CreateModel(
            name='ResumeUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('date_of_brith', models.DateField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('place_of_study', models.JSONField(blank=True, null=True)),
                ('position', models.CharField(blank=True, max_length=255, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('job_experiences', models.JSONField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('job_tag', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentification.jobcategories')),
                ('level_of_education', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentification.leveleducation')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Resume',
                'verbose_name_plural': 'Resumes',
                'db_table': 'table_resumes',
            },
        ),
        migrations.CreateModel(
            name='NotificationJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_seen', models.BooleanField(blank=True, default=False, null=True)),
                ('job_apply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentification.jobapply')),
                ('jobs_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentification.statusapply')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificationjob', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Job Notification',
                'verbose_name_plural': 'Job Notification',
                'db_table': 'table_job_notification',
            },
        ),
        migrations.CreateModel(
            name='JobVacancies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('salary', models.FloatField(blank=True, default=0, null=True)),
                ('qualifications', models.CharField(blank=True, max_length=255, null=True)),
                ('experience', models.BooleanField(blank=True, default=False, null=True)),
                ('work_hours', models.CharField(blank=True, max_length=255, null=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('is_activate', models.BooleanField(blank=True, default=False, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentification.hrcompany')),
                ('is_look_user', models.ManyToManyField(blank=True, null=True, related_name='isLookUser', to=settings.AUTH_USER_MODEL)),
                ('is_seen', models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
                ('job_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categor_id', to='authentification.jobcategories')),
                ('job_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_type', to='authentification.jobtype')),
            ],
            options={
                'verbose_name': 'Vacancy',
                'verbose_name_plural': 'Vacancies',
                'db_table': 'table_vacancy',
            },
        ),
        migrations.AddField(
            model_name='jobapply',
            name='jobs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='authentification.jobvacancies'),
        ),
        migrations.AddField(
            model_name='jobapply',
            name='jobs_status',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentification.statusapply'),
        ),
        migrations.AddField(
            model_name='jobapply',
            name='resume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentification.resumeuser'),
        ),
        migrations.AddField(
            model_name='jobapply',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Favourites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('jobs', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='authentification.jobvacancies')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favourites', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Favourites',
                'verbose_name_plural': 'Favourites',
                'db_table': 'table_favourites',
            },
        ),
        migrations.AddField(
            model_name='customuser',
            name='group',
            field=models.ManyToManyField(blank=True, null=True, to='authentification.role'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
