from flask import redirect, request, url_for, render_template, flash
from flask.views import MethodView
from openai import OpenAI


class Poem(MethodView):
    def get(self):
        # TODO: fix format of poem string for nice output
        poem = self.createPoem(request.args.get("labels"), request.args.get("objects"))
        image_path = request.args.get("image_path")
        return render_template("poem.html", image_path=image_path, poem=poem)

    def createPoem(self, labels, objects):
        client = OpenAI()
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.createSystemRole()},
                {"role": "user", "content": self.createUserPrompt(labels, objects)},
            ],
        )
        print(completion.choices[0].message)
        return completion.choices[0].message

    def createUserPrompt(self, labels, objects):
        prompt = f"Create a poem about {labels} and {objects}. Only ouput the poem in json format with key 'poem'."
        return prompt

    def createSystemRole(self):
        role_prompt = "You are a master artist of poetry who is skilled in creating poems of all styles."
        return role_prompt
