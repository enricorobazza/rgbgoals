# RGB Goals

This is a Example project to test Django and React integration with component as a page.

This project utilizes Webpack to bundle React components and insert the bundles inside Django Templates. 

## Benefits:
- This way, we are able to render a basic page with Django (SSR) and after that we can render the React App (CSR).
- We can populate data as default props to React components without having to load via ajax.
- We can still utilize Django features for rendering front-end, managing routes...
- We can even get a form rendered via Django Templates and pass it as a html string to be rendered inside a React Component.

## Preview:
![RGB Goals Preview](./readme/preview.png)

![RGB Goals Preview - Insert Goal](./readme/add_goal.gif)

![RGB Goals Preview - Update Goal](./readme/update_goal.gif)

## Live:
[https://rgbgoals.herokuapp.com/](https://rgbgoals.herokuapp.com/)


```
Login: example
Password: MyPassword123!
```