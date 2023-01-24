from django import forms

from blog.models import PostComment


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('fullname', 'email', 'website', 'body')

        widgets = {
            "body": forms.Textarea(attrs={"class": 'form-control', "placeholder": 'متن نظر خود را بنویسید ...'}),
            "email": forms.EmailInput(attrs={"class": 'form-control', "placeholder": 'ایمیل خود را بنویسید'}),
            "website": forms.TextInput(attrs={"class": 'form-control', "placeholder": 'وبسایت خود را وارد کنید(اختیاری)'}),
            "fullname": forms.TextInput(attrs={"class": 'form-control', "placeholder": 'نام خود را بنویسید'}),
        }

    def save(self, post, commit=True):
        cd = self.cleaned_data
        post_comment = PostComment(
            post=post, fullname=cd['fullname'], email=cd['email'], website=cd.get('website'),
            body=cd['body']
        )
        if commit:
            post_comment.save()
        return post_comment

