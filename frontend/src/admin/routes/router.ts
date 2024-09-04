import CRUDStreams from '@/admin/views/CRUDStreamsView.vue'
import InstructorsView from '@/admin/views/InstructorsView.vue'


export const adminRoutes = [
  { path: 'streams', component: CRUDStreams, name: 'admin-streams' },
  { path: 'instructors', component: InstructorsView, name: 'instructors' }
]