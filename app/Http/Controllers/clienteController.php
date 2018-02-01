<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class clienteController extends Controller
{
    public function index()
    {
      $sum=5+6;
      //return $sum;
      return view('index');
    }
}
