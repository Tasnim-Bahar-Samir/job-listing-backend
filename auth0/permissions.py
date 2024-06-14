from rest_framework.permissions import BasePermission


class IsCompany(BasePermission):
    def has_permission(self, request, view):
        print(request.user.user_profile.group,666)
        have_companyAccess = request.user.user_profile.group == 'COMPANY'

        if have_companyAccess:
            return True
        else:
            return False


class IsCandidate(BasePermission):
    def has_permission(self, request, view):
        haveCandidateAccess = request.user.user_profile.group == "CANDIDATE"

        if haveCandidateAccess:
            return True
        else:
            return False
