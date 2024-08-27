from django.db import models

# Create your models here.


class Actions(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    title = models.CharField(max_length=255, blank=False)
    REQUIRED_FIELDS = ['name', "title"]

    def str(self) -> str:
        return self.name

    def toDict(self):
        results = {}
        results['name'] = self.name
        results['title'] = self.title
        return results


class Roles(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    actions = models.ForeignKey(
        Actions, on_delete=models.DO_NOTHING, related_name='actions', null=False, blank=False)
    REQUIRED_FIELDS = ['name']

    def str(self) -> str:
        return self.name

    def toDict(self):
        results = {}
        results['name'] = self.name
        return results


class Groups(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    roles = models.ForeignKey(
        Roles, on_delete=models.DO_NOTHING, related_name='roles', null=False, blank=False)
    parent_group = models.CharField(max_length=100, blank=True)

    def str(self) -> str:
        return self.name

    def toDict(self) :
        results = {}
        results['name'] = self.name
        results['parent_group'] = self.parent_group
        return results


class Projects(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    title = models.CharField(max_length=255, blank=False,
                             verbose_name='Display Name')
    description = models.CharField(max_length=255, blank=True)
    REQUIRED_FIELDS = ['name', 'title']

    def str(self) -> str:
        return self.name

    def toDict(self) :
        results = {}
        results['name'] = self.name
        results['title'] = self.title
        results['description'] = self.description
        return results
