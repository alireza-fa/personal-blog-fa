from django import forms

from blog.models import PostComment, Newsletter


class PostCommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostCommentForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['fullname'].required = True

    class Meta:
        model = PostComment
        fields = ('fullname', 'email', 'website', 'body')

        widgets = {
            "body": forms.Textarea(
                attrs={"class": 'form-control', "placeholder": 'متن نظر خود را بنویسید ...', "id": 'body'}),
            "email": forms.EmailInput(
                attrs={"class": 'form-control', "placeholder": 'ایمیل خود را بنویسید', "id": 'email'}),
            "website": forms.TextInput(
                attrs={"class": 'form-control', "placeholder": 'وبسایت خود را وارد کنید(اختیاری)', "id": 'website'}),
            "fullname": forms.TextInput(
                attrs={"class": 'form-control', "placeholder": 'نام خود را بنویسید', "id": 'fullname'}),
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


class NewsletterForm(forms.Form):
    news_email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": 'form-control w-100 text-center', "placeholder": 'ایمیل خود را بنویسید ...', "id": 'news_email'}),
        max_length=120,
    )

    def save(self, commit=True):
        newsletter = Newsletter(email=self.cleaned_data['news_email'])
        if commit:
            newsletter.save()
        return newsletter
