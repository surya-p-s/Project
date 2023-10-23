package com.example.marinesoft

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.auth.ktx.auth
import com.google.firebase.firestore.ktx.firestore
import com.google.firebase.ktx.Firebase

class DataActivity : AppCompatActivity() {
    private lateinit var auth : FirebaseAuth
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_data)

        auth = Firebase.auth
        val logOut=findViewById<Button>(R.id.logOut)

        logOut.setOnClickListener{
            Firebase.auth.signOut()
            updateUI()
        }
    }

    private fun updateUI() {
        val intent= Intent(this,SignInActivity::class.java)
        startActivity(intent)
        finish()
    }
}