package com.example.eblood

import android.content.ContentValues
import android.content.ContentValues.TAG
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.ProgressBar
import android.widget.Toast
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.auth.FirebaseUser
import com.google.firebase.auth.ktx.auth
import com.google.firebase.ktx.Firebase

class LogInPage : AppCompatActivity() {
    private lateinit var auth : FirebaseAuth
    private lateinit var email : EditText
    private lateinit var password : EditText
    private lateinit var logIn : Button

    private lateinit var sEmail : String
    private lateinit var sPassword : String

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_log_in_page)

        auth = Firebase.auth
        val registerButton=findViewById<Button>(R.id.registerButton1)
        logIn = findViewById(R.id.logIn)
        email = findViewById(R.id.emailText1)
        password = findViewById(R.id.textPassword1)



        logIn.setOnClickListener {

            sEmail = email.text.toString().trim()
            sPassword = password.text.toString().trim()


            auth.signInWithEmailAndPassword(sEmail, sPassword)
                .addOnCompleteListener(this) { task ->
                    if (task.isSuccessful) {
                        Log.d(TAG, "signInWithEmail:success")
                        Toast.makeText(baseContext, "LogIn Successful", Toast.LENGTH_SHORT)
                            .show()
                        val user = auth.currentUser
                        updateUI(user)
                    } else {
                        Log.w(TAG, "signInWithEmail:failure", task.exception)
                        Toast.makeText(baseContext, "Try again OR Register", Toast.LENGTH_SHORT)
                            .show()
                    }
                }
        }
        registerButton.setOnClickListener {
            val intent= Intent(this,Register::class.java)
            startActivity(intent)
        }
    }

    override fun onStart() {
        super.onStart()

        val currentUser=auth.currentUser

        if (currentUser!=null){

            val intent= Intent(this,DataPage::class.java)
            startActivity(intent)
            finish()
        }
    }

    private fun updateUI(user: FirebaseUser?) {
        if(user != null) {
            val intent = Intent(this, DataPage::class.java)
            startActivity(intent)
            finish()
        }
    }
}