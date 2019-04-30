import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RegistarPage } from './registar.page';

describe('RegistarPage', () => {
  let component: RegistarPage;
  let fixture: ComponentFixture<RegistarPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RegistarPage ],
      schemas: [CUSTOM_ELEMENTS_SCHEMA],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RegistarPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
