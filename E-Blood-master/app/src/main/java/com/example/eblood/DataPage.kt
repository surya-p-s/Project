package com.example.eblood

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.ArrayAdapter
import android.widget.Button
import android.widget.ProgressBar
import android.widget.Spinner
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.auth.ktx.auth
import com.google.firebase.ktx.Firebase

class DataPage : AppCompatActivity() {
    private lateinit var auth : FirebaseAuth
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_data_page)

        auth = Firebase.auth
        val logOut=findViewById<Button>(R.id.logOut)

        logOut.setOnClickListener{
            Firebase.auth.signOut()
            updateUI()
        }

        val editButton=findViewById<Button>(R.id.button2)
        editButton.setOnClickListener {
            val intent = Intent(this,DetailsActivity::class.java)
            startActivity(intent)
        }

    }
    private fun updateUI() {
        val intent= Intent(this,LogInPage::class.java)
        startActivity(intent)
        finish()
    }
}