import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { VcPage } from './vc.page';

describe('VcPage', () => {
  let component: VcPage;
  let fixture: ComponentFixture<VcPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ VcPage ],
      schemas: [CUSTOM_ELEMENTS_SCHEMA],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(VcPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
