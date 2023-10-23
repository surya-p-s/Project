package com.example.eblood

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button

class DetailsActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_details)

        val submitButton = findViewById<Button>(R.id.button)

        submitButton.setOnClickListener {
            val intent = Intent(this,DataPage::class.java)
            startActivity(intent)
            finish()
        }
    }
}