from rest_framework.permissions import BasePermission


class IsCompany(BasePermission):
    def has_permission(self, request, view):
        have_companyAccess = request.user.user_profile.group.all().filter(name="company").exists()

        if have_companyAccess:
            return True
        else:
            return False


class IsCandidate(BasePermission):
    def has_permission(self, request, view):
        haveCandidateAccess = request.user.user_profile.group.all().filter(name="candidate").exists()

        if haveCandidateAccess:
            return True
        else:
            return False
