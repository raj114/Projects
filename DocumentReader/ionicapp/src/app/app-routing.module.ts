import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: 'home', loadChildren: './home/home.module#HomePageModule' },
  { path: 'Register', loadChildren: './register/register.module#RegisterPageModule' },
  { path: 'Student/:username', loadChildren: './student/student.module#StudentPageModule' },
  { path: 'Office/:username', loadChildren: './office/office.module#OfficePageModule' },
  { path: 'Registar/:username', loadChildren: './registar/registar.module#RegistarPageModule' },
  { path: 'VC/:username/', loadChildren: './vc/vc.module#VcPageModule' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
