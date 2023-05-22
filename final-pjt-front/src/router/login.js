import SignUpView from '../views/SignUpView'
import LoginView from '../views/LoginView'

export default [

  {
    path: '/signup',
    name:'SignUpView',
    component: SignUpView
  },
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView,
  }

]