﻿using System.ComponentModel.DataAnnotations;

namespace Demo.PL.ViewModels
{
    public class SignInViewModel
    {
        [Required(ErrorMessage = "Email is Required.")]
        [EmailAddress(ErrorMessage = "Invalid Email.")]
        public string Email { get; set; }


        [Required(ErrorMessage = "Password is Required")]
        [DataType(DataType.Password)]
        [MinLength(7, ErrorMessage = "Minimum Length is 7")] 
        public string Password { get; set; }

        public bool RememberMe { get; set; }
    }
}
