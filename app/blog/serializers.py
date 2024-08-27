from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers
from accounts.models import User
import json
from blog.models import Actions, Projects, Groups, Roles


class CreateActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actions
        fields = ['name', 'title']

    def create(self, attrs):
        try:
            action = Actions.objects.create(name=attrs['name'])
        except:
            return "item exist"
        action.title = attrs['title']

        action.save()
        return attrs


class CreateRolesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Roles
        fields = ['name']

    def create(self, attrs):

        try:
            roleId = Actions.objects.get(name=attrs['actions']).id
        except:
            return "role is missing"

        try:
            roles = Roles.objects.create(name=attrs['name'], actions_id=roleId)
        except Exception as e:
            print(e)
            return "item exist"

        roles.save()
        return "saved"


class CreateGroupsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Groups
        fields = ['name', 'role', 'parent_group']

    def create(self, attrs):
        try:
            roleId = Roles.objects.get(name=attrs['role']).id
        except:
            return "role is missing"
        try:
            group = Groups.objects.create(name=attrs['name'], roles_id=roleId)
        except:
            return "item exist"

        group.parent_group = attrs['parent_group']
        group.save()
        return attrs


class CreateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['name', 'title', 'description']

    def create(self, attrs):
        try:
            projects = Projects.objects.create(name=attrs['name'])
        except:
            return "item exist"
        projects.title = attrs['title']
        projects.description = attrs['description']
        projects.save()
        return attrs


class BlogGetSerializer(serializers.ModelSerializer):
    class Meta:
        fields = []

    def create(self, attrs):
        results = {}

        if 'action' in attrs:
            try:
                action = Actions.objects.get(name=attrs['action'])
            except:
                pass
            try:
                role = Roles.objects.filter(actions_id=action.id).values()
                roles = []
                for i in role:
                    roles.append(i)
            except Exception as e:
                pass
            try:
                print(roles[0])
                group = Groups.objects.filter(roles=roles[0]['id']).values()
                groups = []
                for i in group:
                    groups.append(i)
            except Exception as e:
                pass
            try:
                results['action'] = str(action.toDict())
            except:
                pass
            try:
                results['role'] = str(roles)
            except:
                pass
            try:
                results['groups'] = str(groups)
            except:
                pass
            return results

        if 'role' in attrs:
            try:
                role = Roles.objects.get(name=attrs['role'])
            except:
                return "role is missing"
            try:
                
                group = Groups.objects.filter(roles=role.id).values()
                groups = []
                for i in group:
                    groups.append(i)
            except:
                pass
            try:
                results['role'] = str(role.toDict())
            except:
                pass
            try:
                results['groups'] = str(groups)
            except:
                pass

            return results

        if 'group' in attrs:
            try:
                groups = Groups.objects.get(name=attrs['group'])
                results['groups'] = str(groups.toDict())
            except:
                return "group is missing"

            return results

        if 'project' in attrs:
            try:
                project = Projects.objects.get(name=attrs['project'])
                results['project'] = str(project.toDict())
            except:
                pass

            return results

        return results
