import HomeView from '@/shared/views/HomeView.vue'
import StreamView from '@/default/views/StreamView.vue'
import InstructorsDefaultView from '@/default/views/InstructorsView.vue'
import InstructorView from '@/default/views/InstructorView.vue'


export const routes = [
  { path: '', component: HomeView, name: 'home' },
  { path: 'streams/:id', component: StreamView, name: 'streams' },
  { path: 'instructors', component: InstructorsDefaultView, name: 'instructors-default' },
  { path: 'instructor/:id', component: InstructorView, name: 'instructor' }
]