package com.example.marinesoftapplication

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.google.android.material.navigation.NavigationBarItemView
import com.google.firebase.auth.ktx.auth
import com.google.firebase.ktx.Firebase

class GraphActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_graph)

        //        navigation

        val signOut=findViewById<NavigationBarItemView>(R.id.signOut)
        val analytic=findViewById<NavigationBarItemView>(R.id.analytic)
        val graph=findViewById<NavigationBarItemView>(R.id.graph)
        val uploadButton=findViewById<NavigationBarItemView>(R.id.imageUpload)
        val home=findViewById<NavigationBarItemView>(R.id.home_menu)

        home.setOnClickListener {
            startActivity(Intent(this,DataActivity::class.java))
        }

        analytic.setOnClickListener {
            startActivity(Intent(this, AnalyticActivity::class.java))
        }
        // Authentiation
        signOut.setOnClickListener{
            Firebase.auth.signOut()
            updateUI()
        }
        uploadButton.setOnClickListener {
            val intent= Intent(this,UploadActivity::class.java)
            startActivity(intent)
        }
    }

    private fun updateUI() {
        val intent= Intent(this,SignInPage::class.java)
        startActivity(intent)
        finish()
    }
}