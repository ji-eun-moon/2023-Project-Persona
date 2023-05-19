import CreateView from '../components/community/CreateView.vue'
import DetailView from '../components/community/DetailView.vue'
import UpdateView from '../components/community/UpdateView.vue'

export default [
  {
    path: '/community/reviews/create',
    name:'CreateView',
    component: CreateView
  },
  {
    path: '/community/reviews/:id',
    name:'DetailView',
    component: DetailView,
  },
  {
    path: '/community/reviews/:id/update',
    name:'UpdateView',
    component: UpdateView,
  }
]